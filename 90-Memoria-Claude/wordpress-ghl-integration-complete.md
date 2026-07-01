---
name: WordPress-GHL Integration — Guía Completa
description: Forms, tracking, CRM webhook handlers, ejemplos
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# WordPress-GHL Integration — Guía Completa

## 1. Introducción a WordPress-GHL

**Integración:** WordPress (blog/landing) → GHL (CRM).

**Flujos:**
- Contact form submission → crear contacto en GHL
- Comentario en blog → trigger workflow
- Lead form → crear oportunidad
- Email optin → agregar a lista

---

## 2. Inyectar Meta Pixel en WordPress

### Via Plugin (WPCode)

1. Instalar plugin "WPCode"
2. Dashboard → Code Snippets → Add Snippet
3. Tipo: HTML
4. Agregar Meta Pixel:

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');

fbq('init', '1625645205284016'); // Reemplazar con tu pixel
fbq('track', 'PageView');
</script>

<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1625645205284016&ev=PageView&noscript=1"
/>
</noscript>
```

### Via functions.php

```php
// En wp-content/themes/your-theme/functions.php

add_action('wp_head', 'add_meta_pixel');
function add_meta_pixel() {
    ?>
    <!-- Meta Pixel -->
    <script>
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');

    fbq('init', '1625645205284016');
    fbq('track', 'PageView');
    </script>
    <?php
}
```

---

## 3. Contact Form 7 Integration

### Capturar Form7 Submissions

```php
// En functions.php

add_action('wpcf7_mail_sent', 'send_cf7_to_ghl');
function send_cf7_to_ghl(WPCF7_ContactForm $contact_form) {
    $submission = WPCF7_Submission::get_instance();
    
    if (!$submission) return;
    
    $posted_data = $submission->get_posted_data();
    
    // Preparar datos para GHL
    $ghl_data = [
        'firstName' => $posted_data['your-name'][0] ?? 'Lead',
        'email' => $posted_data['your-email'][0] ?? '',
        'phone' => $posted_data['your-phone'][0] ?? '',
        'message' => $posted_data['your-message'][0] ?? '',
        'source' => 'wordpress_cf7',
        'tags' => ['web_lead', 'contact_form'],
        'customFields' => [
            'form_name' => $contact_form->get_title(),
            'page_url' => $_SERVER['HTTP_REFERER'] ?? '',
            'utm_source' => $_GET['utm_source'] ?? '',
            'utm_medium' => $_GET['utm_medium'] ?? '',
            'utm_campaign' => $_GET['utm_campaign'] ?? ''
        ]
    ];
    
    // Enviar a GHL
    send_to_ghl($ghl_data);
}

function send_to_ghl($data) {
    $api_key = 'YOUR_GHL_API_KEY';
    $location_id = 'YOUR_LOCATION_ID';
    
    $url = 'https://rest.gohighlevel.com/v1/contacts/';
    
    $args = [
        'method' => 'POST',
        'headers' => [
            'Authorization' => "Bearer $api_key",
            'Content-Type' => 'application/json'
        ],
        'body' => json_encode(array_merge($data, ['locationId' => $location_id]))
    ];
    
    $response = wp_remote_post($url, $args);
    
    if (is_wp_error($response)) {
        error_log('GHL Error: ' . $response->get_error_message());
    } else {
        error_log('GHL Success: ' . wp_remote_retrieve_body($response));
    }
}
```

---

## 4. WooCommerce Integration

### Track Order Creation

```php
// En functions.php

add_action('woocommerce_new_order', 'send_order_to_ghl');
function send_order_to_ghl($order_id) {
    $order = wc_get_order($order_id);
    
    $ghl_data = [
        'firstName' => $order->get_billing_first_name(),
        'lastName' => $order->get_billing_last_name(),
        'email' => $order->get_billing_email(),
        'phone' => $order->get_billing_phone(),
        'tags' => ['woocommerce_buyer'],
        'customFields' => [
            'order_id' => $order_id,
            'order_total' => $order->get_total(),
            'order_status' => $order->get_status(),
            'order_items' => implode(', ', wp_list_pluck($order->get_items(), 'name'))
        ]
    ];
    
    send_to_ghl($ghl_data);
}
```

### Track Product Views

```php
// En functions.php

add_action('wp_footer', 'track_product_views');
function track_product_views() {
    if (is_product()) {
        global $product;
        
        // Track Meta Pixel
        ?>
        <script>
        fbq('track', 'ViewContent', {
            content_ids: ['<?php echo $product->get_id(); ?>'],
            content_type: 'product',
            content_name: '<?php echo $product->get_name(); ?>',
            value: <?php echo $product->get_price(); ?>,
            currency: 'USD'
        });
        </script>
        <?php
    }
}
```

---

## 5. Gravity Forms Integration

### Capturar Gravity Forms Submissions

```php
// En functions.php

add_action('gform_after_submission', 'send_gravity_form_to_ghl', 10, 2);
function send_gravity_form_to_ghl($entry, $form) {
    // Mapear campos de Gravity Forms
    $ghl_data = [
        'firstName' => rgar($entry, '1'),  // Campo ID 1
        'email' => rgar($entry, '2'),      // Campo ID 2
        'phone' => rgar($entry, '3'),      // Campo ID 3
        'message' => rgar($entry, '4'),    // Campo ID 4
        'source' => 'wordpress_gravity_forms',
        'tags' => ['web_lead', 'gravity_form'],
        'customFields' => [
            'form_name' => $form['title'],
            'form_id' => $form['id']
        ]
    ];
    
    send_to_ghl($ghl_data);
}
```

---

## 6. Webhook Handler — Recibir de GHL

### Registrar webhook endpoint

```php
// En functions.php

add_action('init', 'register_ghl_webhook_endpoint');
function register_ghl_webhook_endpoint() {
    add_rewrite_rule(
        '^ghl-webhook/?$',
        'index.php?ghl_webhook=1',
        'top'
    );
}

add_filter('query_vars', 'add_ghl_webhook_query_var');
function add_ghl_webhook_query_var($vars) {
    $vars[] = 'ghl_webhook';
    return $vars;
}

add_action('template_redirect', 'handle_ghl_webhook');
function handle_ghl_webhook() {
    global $wp_query;
    
    if (!isset($wp_query->query_vars['ghl_webhook'])) return;
    
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        status_header(405);
        die('Method Not Allowed');
    }
    
    $payload = json_decode(file_get_contents('php://input'), true);
    
    // Verificar signature
    $signature = $_SERVER['HTTP_X_GHL_SIGNATURE'] ?? '';
    if (!verify_ghl_signature($payload, $signature)) {
        status_header(401);
        die('Unauthorized');
    }
    
    // Procesar webhook
    process_ghl_webhook($payload);
    
    // Responder a GHL
    header('Content-Type: application/json');
    echo json_encode(['success' => true]);
    die;
}

function verify_ghl_signature($payload, $signature) {
    $secret = 'YOUR_GHL_WEBHOOK_SECRET';
    $body = json_encode($payload);
    $expected = hash_hmac('sha256', $body, $secret);
    return hash_equals($expected, $signature);
}

function process_ghl_webhook($payload) {
    // Procesar evento de GHL
    $event = $payload['eventType'] ?? '';
    
    if ($event === 'contact.created') {
        // Crear post, enviar email, etc.
        error_log('New contact created: ' . $payload['contactId']);
    } elseif ($event === 'contact.updated') {
        error_log('Contact updated: ' . $payload['contactId']);
    }
}
```

---

## 7. Formulario Custom con GHL Integration

```php
// En wp-content/plugins/my-plugin/my-plugin.php

<?php
/**
 * Plugin Name: GHL Lead Capture
 * Description: Captura leads y los envía a GHL
 */

if (!defined('ABSPATH')) exit;

// Enqueue scripts
add_action('wp_enqueue_scripts', 'ghl_capture_enqueue_scripts');
function ghl_capture_enqueue_scripts() {
    wp_enqueue_script(
        'ghl-capture',
        plugin_dir_url(__FILE__) . 'js/capture.js',
        [],
        '1.0',
        true
    );
    
    wp_localize_script('ghl-capture', 'ghlData', [
        'ajaxUrl' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('ghl_nonce')
    ]);
}

// Shortcode: [ghl_form]
add_shortcode('ghl_form', 'ghl_lead_form_shortcode');
function ghl_lead_form_shortcode() {
    ob_start();
    ?>
    <form id="ghl-lead-form" class="ghl-form">
        <div class="form-group">
            <label>Name:</label>
            <input type="text" name="name" required>
        </div>
        
        <div class="form-group">
            <label>Email:</label>
            <input type="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label>Phone:</label>
            <input type="tel" name="phone" required>
        </div>
        
        <div class="form-group">
            <label>Message:</label>
            <textarea name="message" rows="5"></textarea>
        </div>
        
        <button type="submit" class="btn">Send</button>
        <div id="form-message"></div>
    </form>
    
    <style>
        .ghl-form {
            max-width: 500px;
            margin: 20px 0;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
        }
        
        .ghl-form button {
            background: #0066cc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        
        .ghl-form button:hover {
            background: #0052a3;
        }
    </style>
    <?php
    return ob_get_clean();
}

// AJAX Handler
add_action('wp_ajax_ghl_submit_form', 'ghl_handle_form_submission');
add_action('wp_ajax_nopriv_ghl_submit_form', 'ghl_handle_form_submission');

function ghl_handle_form_submission() {
    check_ajax_referer('ghl_nonce');
    
    $name = sanitize_text_field($_POST['name'] ?? '');
    $email = sanitize_email($_POST['email'] ?? '');
    $phone = sanitize_text_field($_POST['phone'] ?? '');
    $message = sanitize_textarea_field($_POST['message'] ?? '');
    
    if (!$email) {
        wp_send_json_error('Email is required');
    }
    
    // Enviar a GHL
    $ghl_data = [
        'firstName' => $name,
        'email' => $email,
        'phone' => $phone,
        'message' => $message,
        'source' => 'wordpress_form',
        'tags' => ['web_lead']
    ];
    
    $result = send_to_ghl($ghl_data);
    
    if ($result) {
        wp_send_json_success('Thank you! We will contact you soon.');
    } else {
        wp_send_json_error('Error sending form. Please try again.');
    }
}

function send_to_ghl($data) {
    $api_key = get_option('ghl_api_key');
    $location_id = get_option('ghl_location_id');
    
    if (!$api_key || !$location_id) {
        error_log('GHL API key or location ID not configured');
        return false;
    }
    
    $url = 'https://rest.gohighlevel.com/v1/contacts/';
    
    $args = [
        'method' => 'POST',
        'headers' => [
            'Authorization' => "Bearer $api_key",
            'Content-Type' => 'application/json'
        ],
        'body' => json_encode(array_merge($data, ['locationId' => $location_id]))
    ];
    
    $response = wp_remote_post($url, $args);
    
    return !is_wp_error($response);
}
```

---

## 8. JavaScript Frontend (AJAX)

```javascript
// wp-content/plugins/my-plugin/js/capture.js

jQuery(document).ready(function($) {
    $('#ghl-lead-form').on('submit', function(e) {
        e.preventDefault();
        
        const form = $(this);
        const data = {
            action: 'ghl_submit_form',
            nonce: ghlData.nonce,
            name: form.find('[name="name"]').val(),
            email: form.find('[name="email"]').val(),
            phone: form.find('[name="phone"]').val(),
            message: form.find('[name="message"]').val()
        };
        
        $.ajax({
            type: 'POST',
            url: ghlData.ajaxUrl,
            data: data,
            success: function(response) {
                if (response.success) {
                    $('#form-message').html('<p style="color: green;">' + response.data + '</p>');
                    form[0].reset();
                } else {
                    $('#form-message').html('<p style="color: red;">' + response.data + '</p>');
                }
            },
            error: function() {
                $('#form-message').html('<p style="color: red;">Error occurred</p>');
            }
        });
    });
});
```

---

## 9. Settings Page para GHL API

```php
// En functions.php

add_action('admin_menu', 'ghl_add_settings_menu');
function ghl_add_settings_menu() {
    add_options_page(
        'GHL Settings',
        'GHL Settings',
        'manage_options',
        'ghl_settings',
        'ghl_settings_page'
    );
}

function ghl_settings_page() {
    if (!current_user_can('manage_options')) return;
    
    if ($_POST && check_admin_referer('ghl_settings_nonce')) {
        update_option('ghl_api_key', sanitize_text_field($_POST['api_key']));
        update_option('ghl_location_id', sanitize_text_field($_POST['location_id']));
        echo '<div class="notice notice-success"><p>Settings saved!</p></div>';
    }
    
    $api_key = get_option('ghl_api_key');
    $location_id = get_option('ghl_location_id');
    ?>
    <div class="wrap">
        <h1>GHL Integration Settings</h1>
        <form method="post">
            <?php wp_nonce_field('ghl_settings_nonce'); ?>
            <table class="form-table">
                <tr>
                    <th><label for="api_key">API Key:</label></th>
                    <td>
                        <input type="password" name="api_key" id="api_key" 
                               value="<?php echo esc_attr($api_key); ?>" class="regular-text">
                    </td>
                </tr>
                <tr>
                    <th><label for="location_id">Location ID:</label></th>
                    <td>
                        <input type="text" name="location_id" id="location_id" 
                               value="<?php echo esc_attr($location_id); ?>" class="regular-text">
                    </td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>
    </div>
    <?php
}
```

---

## 10. Gotchas WordPress-GHL

### Problema: AJAX falla

**Solución:** Verificar nonce y que ajaxUrl está correcto.

### Problema: Custom fields no se sincan

**Solución:** Mapear correctamente field IDs de GHL.

### Problema: Duplicados de contactos

**Solución:** Usar upsert endpoint en lugar de create.

---

## 11. Recursos

- [WP Plugin Development](https://developer.wordpress.org/plugins/)
- [GHL REST API](https://docs.gohighlevel.com/api/)
- [WP AJAX](https://developer.wordpress.org/plugins/javascript/ajax/)

