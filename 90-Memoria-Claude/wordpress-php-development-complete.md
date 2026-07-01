---
name: WordPress PHP Development — Guía Completa
description: PHP, hooks, custom post types, WooCommerce, seguridad, ejemplos copy-paste
metadata:
  type: technical-reference
  version: "1.0"
  updated: "2026-06-30"
---

# WordPress PHP Development — Guía Completa

## 1. Estructura de un Plugin WordPress

```
my-plugin/
├── my-plugin.php           # Archivo principal
├── includes/
│   ├── class-plugin.php
│   ├── class-admin.php
│   └── functions.php
├── public/
│   ├── js/
│   │   └── script.js
│   ├── css/
│   │   └── style.css
│   └── class-public.php
├── admin/
│   ├── js/
│   │   └── admin-script.js
│   ├── css/
│   │   └── admin-style.css
│   └── class-admin.php
└── readme.txt
```

### Archivo Principal (my-plugin.php)

```php
<?php
/**
 * Plugin Name: My Custom Plugin
 * Description: A custom plugin for Innovart
 * Version: 1.0.0
 * Author: Javier Forero
 * License: GPL-2.0+
 * Text Domain: my-plugin
 * Domain Path: /languages
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

define( 'MY_PLUGIN_PATH', plugin_dir_path( __FILE__ ) );
define( 'MY_PLUGIN_URL', plugin_dir_url( __FILE__ ) );

// Cargar archivo principal
require_once MY_PLUGIN_PATH . 'includes/class-plugin.php';

// Iniciar plugin
function my_plugin_init() {
    $plugin = new My_Plugin();
    $plugin->run();
}
add_action( 'plugins_loaded', 'my_plugin_init' );

// Activación
register_activation_hook( __FILE__, 'my_plugin_activate' );
function my_plugin_activate() {
    // Crear tablas, opciones, etc.
    update_option( 'my_plugin_version', '1.0.0' );
}

// Desactivación
register_deactivation_hook( __FILE__, 'my_plugin_deactivate' );
function my_plugin_deactivate() {
    // Limpiar datos si es necesario
}
```

---

## 2. Hooks — Actions y Filters

### Actions (Ejecución)

```php
// Hook personalizado
do_action( 'my_plugin_custom_event', $variable1, $variable2 );

// Subscribirse a un action
add_action( 'wp_footer', 'my_plugin_footer_code' );
function my_plugin_footer_code() {
    echo '<p>Footer custom code</p>';
}

// Acciones de WordPress comunes
add_action( 'wp_enqueue_scripts', 'my_plugin_enqueue_assets' );
add_action( 'admin_enqueue_scripts', 'my_plugin_admin_assets' );
add_action( 'init', 'my_plugin_register_post_type' );
add_action( 'wp_head', 'my_plugin_head_content' );
```

### Filters (Modificación)

```php
// Hook personalizado
$result = apply_filters( 'my_plugin_filter_output', $output );

// Subscribirse a un filter
add_filter( 'the_content', 'my_plugin_modify_content' );
function my_plugin_modify_content( $content ) {
    return $content . '<p>Agregado al final</p>';
}

// Filters comunes
add_filter( 'wp_title', 'my_plugin_custom_title' );
add_filter( 'excerpt_length', 'my_plugin_excerpt_length' );
add_filter( 'body_class', 'my_plugin_body_class' );
```

### Prioridad en Hooks

```php
// Prioridad por defecto: 10
add_filter( 'the_content', 'filter_a' );              // 10
add_filter( 'the_content', 'filter_b', 5 );           // 5 (ejecuta primero)
add_filter( 'the_content', 'filter_c', 20 );          // 20 (ejecuta último)

// Numero de parámetros
add_filter( 'my_hook', 'my_function', 10, 2 );  // 2 parámetros
function my_function( $param1, $param2 ) {
    return $param1 . ' - ' . $param2;
}
```

---

## 3. Enqueuing Scripts y Styles

### Enqueue en el Frontend

```php
add_action( 'wp_enqueue_scripts', 'my_plugin_enqueue_assets' );
function my_plugin_enqueue_assets() {
    // CSS
    wp_enqueue_style(
        'my-plugin-style',
        MY_PLUGIN_URL . 'public/css/style.css',
        [],
        '1.0.0',
        'all'
    );
    
    // JavaScript
    wp_enqueue_script(
        'my-plugin-script',
        MY_PLUGIN_URL . 'public/js/script.js',
        [ 'jquery' ],  // Dependencias
        '1.0.0',
        true           // En el footer
    );
    
    // Localizar variables para JavaScript
    wp_localize_script(
        'my-plugin-script',
        'myPluginData',
        [
            'ajaxUrl' => admin_url( 'admin-ajax.php' ),
            'nonce' => wp_create_nonce( 'my_plugin_nonce' ),
        ]
    );
}
```

### Enqueue en Admin

```php
add_action( 'admin_enqueue_scripts', 'my_plugin_admin_assets' );
function my_plugin_admin_assets() {
    wp_enqueue_style(
        'my-plugin-admin-style',
        MY_PLUGIN_URL . 'admin/css/admin-style.css'
    );
    
    wp_enqueue_script(
        'my-plugin-admin-script',
        MY_PLUGIN_URL . 'admin/js/admin-script.js'
    );
}
```

---

## 4. Custom Post Types

```php
add_action( 'init', 'my_plugin_register_post_type' );
function my_plugin_register_post_type() {
    $args = [
        'label' => 'Testimonials',
        'public' => true,
        'has_archive' => true,
        'menu_icon' => 'dashicons-star-filled',
        'supports' => [ 'title', 'editor', 'thumbnail', 'custom-fields' ],
        'taxonomies' => [ 'category', 'post_tag' ],
        'rewrite' => [ 'slug' => 'testimonials' ],
    ];
    
    register_post_type( 'testimonial', $args );
}

// Registrar taxonomía
add_action( 'init', 'my_plugin_register_taxonomy' );
function my_plugin_register_taxonomy() {
    register_taxonomy(
        'testimonial_category',
        'testimonial',
        [
            'label' => 'Categories',
            'public' => true,
            'hierarchical' => true,
        ]
    );
}
```

---

## 5. Meta Boxes (Campos Personalizados)

```php
add_action( 'add_meta_boxes', 'my_plugin_add_meta_boxes' );
function my_plugin_add_meta_boxes() {
    add_meta_box(
        'my_plugin_meta_box',
        'Product Details',
        'my_plugin_render_meta_box',
        'product',
        'normal',
        'default'
    );
}

function my_plugin_render_meta_box( $post ) {
    $value = get_post_meta( $post->ID, '_my_custom_field', true );
    wp_nonce_field( 'my_plugin_nonce', 'my_plugin_nonce' );
    ?>
    <label for="my_field">Custom Field:</label>
    <input 
        type="text" 
        id="my_field" 
        name="my_field" 
        value="<?php echo esc_attr( $value ); ?>"
    >
    <?php
}

// Guardar meta
add_action( 'save_post', 'my_plugin_save_meta' );
function my_plugin_save_meta( $post_id ) {
    if ( ! isset( $_POST['my_plugin_nonce'] ) ) {
        return;
    }
    
    if ( ! wp_verify_nonce( $_POST['my_plugin_nonce'], 'my_plugin_nonce' ) ) {
        return;
    }
    
    if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
        return;
    }
    
    if ( isset( $_POST['my_field'] ) ) {
        update_post_meta(
            $post_id,
            '_my_custom_field',
            sanitize_text_field( $_POST['my_field'] )
        );
    }
}
```

---

## 6. Admin Pages y Forms

```php
add_action( 'admin_menu', 'my_plugin_add_admin_page' );
function my_plugin_add_admin_page() {
    add_menu_page(
        'My Plugin Settings',
        'My Plugin',
        'manage_options',
        'my_plugin_settings',
        'my_plugin_settings_page',
        'dashicons-cog'
    );
}

function my_plugin_settings_page() {
    if ( ! current_user_can( 'manage_options' ) ) {
        return;
    }
    
    // Guardar opciones
    if ( isset( $_POST['submit'] ) ) {
        check_admin_referer( 'my_plugin_nonce', 'my_plugin_nonce_field' );
        update_option( 'my_plugin_option', sanitize_text_field( $_POST['option'] ) );
        echo '<div class="notice notice-success"><p>Saved!</p></div>';
    }
    
    $value = get_option( 'my_plugin_option' );
    ?>
    <div class="wrap">
        <h1>My Plugin Settings</h1>
        <form method="post">
            <?php wp_nonce_field( 'my_plugin_nonce', 'my_plugin_nonce_field' ); ?>
            
            <table class="form-table">
                <tr>
                    <th><label for="option">Option:</label></th>
                    <td>
                        <input 
                            type="text" 
                            id="option" 
                            name="option" 
                            value="<?php echo esc_attr( $value ); ?>"
                        >
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

## 7. AJAX en WordPress

### PHP (Lado del servidor)

```php
// Enqueue script con nonce
add_action( 'wp_enqueue_scripts', 'my_plugin_enqueue_ajax' );
function my_plugin_enqueue_ajax() {
    wp_enqueue_script( 'my-ajax-script', MY_PLUGIN_URL . 'public/js/ajax.js' );
    wp_localize_script( 'my-ajax-script', 'myAjax', [
        'ajaxUrl' => admin_url( 'admin-ajax.php' ),
        'nonce' => wp_create_nonce( 'my_nonce' ),
    ]);
}

// Hook AJAX
add_action( 'wp_ajax_my_action', 'my_plugin_ajax_handler' );
add_action( 'wp_ajax_nopriv_my_action', 'my_plugin_ajax_handler' ); // Sin login

function my_plugin_ajax_handler() {
    check_ajax_referer( 'my_nonce' );
    
    $product_id = intval( $_POST['product_id'] );
    $product = wc_get_product( $product_id );
    
    wp_send_json_success( [
        'title' => $product->get_name(),
        'price' => $product->get_price(),
    ]);
}
```

### JavaScript (Lado del cliente)

```javascript
// En public/js/ajax.js
jQuery(document).ready(function($) {
    $('#my-button').on('click', function() {
        $.ajax({
            url: myAjax.ajaxUrl,
            type: 'POST',
            data: {
                action: 'my_action',
                product_id: 123,
                _wpnonce: myAjax.nonce
            },
            success: function(response) {
                if (response.success) {
                    console.log(response.data);
                }
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});
```

---

## 8. Child Themes

**Estructura:**

```
my-child-theme/
├── style.css
├── functions.php
├── template-parts/
├── template-redirect.php
└── (sobrescribir archivos del parent)
```

**style.css:**

```css
/*
 * Theme Name: My Child Theme
 * Theme URI: http://example.com/my-child-theme
 * Description: Child theme of Example Parent Theme
 * Version: 1.0.0
 * Text Domain: my-child-theme
 * Domain Path: /languages
 * Parent: parent-theme-slug
 */
```

**functions.php:**

```php
<?php
// Enqueue parent theme styles
add_action( 'wp_enqueue_scripts', 'my_child_enqueue_styles', 9 );
function my_child_enqueue_styles() {
    wp_enqueue_style(
        'parent-style',
        get_template_directory_uri() . '/style.css'
    );
    
    wp_enqueue_style(
        'child-style',
        get_stylesheet_uri()
    );
}

// Sobrescribir funciones del parent
function parent_function() {
    // Nuevo comportamiento
}
```

---

## 9. WooCommerce Integration

### Custom Product Type

```php
add_filter( 'product_type_selector', 'add_custom_product_type' );
function add_custom_product_type( $types ) {
    $types['custom_product'] = 'Custom Product';
    return $types;
}

// Lógica del producto
add_action( 'woocommerce_process_product_meta_custom_product', 'process_custom_product' );
function process_custom_product( $post_id ) {
    // Procesar datos personalizados
}
```

### Custom Checkout Field

```php
add_filter( 'woocommerce_checkout_fields', 'custom_checkout_fields' );
function custom_checkout_fields( $fields ) {
    $fields['billing']['custom_field'] = [
        'type' => 'text',
        'label' => __( 'Custom Field', 'woocommerce' ),
        'placeholder' => __( 'Enter value', 'woocommerce' ),
        'required' => true,
    ];
    
    return $fields;
}

// Guardar valor en orden
add_action( 'woocommerce_checkout_process', 'validate_custom_field' );
function validate_custom_field() {
    if ( ! isset( $_POST['post_data'] ) ) {
        parse_str( $_POST['post_data'], $post_data );
    }
    
    if ( empty( $_POST['custom_field'] ) ) {
        wc_add_notice( 'Custom field is required', 'error' );
    }
}

add_action( 'woocommerce_checkout_update_order_meta', 'save_custom_field' );
function save_custom_field( $order_id ) {
    if ( ! empty( $_POST['custom_field'] ) ) {
        update_post_meta(
            $order_id,
            '_custom_field',
            sanitize_text_field( $_POST['custom_field'] )
        );
    }
}
```

---

## 10. Seguridad en WordPress

### Nonces

```php
// Crear nonce
wp_nonce_field( 'my_action', 'my_nonce_field' );

// Verificar nonce
if ( ! wp_verify_nonce( $_POST['my_nonce_field'], 'my_action' ) ) {
    wp_die( 'Security check failed' );
}
```

### Sanitización

```php
// Input
$input = sanitize_text_field( $_POST['user_input'] );
$email = sanitize_email( $_POST['email'] );
$url = esc_url( $_POST['url'] );
$html = wp_kses_post( $_POST['html'] );

// Validación
if ( ! is_email( $email ) ) {
    wp_die( 'Invalid email' );
}

if ( ! in_array( $value, [ 'option1', 'option2' ], true ) ) {
    wp_die( 'Invalid option' );
}
```

### Output Escaping

```php
// HTML
echo wp_kses_post( $html );

// Texto
echo esc_html( $text );

// Atributos
echo esc_attr( $attr );

// URL
echo esc_url( $url );

// JavaScript
echo wp_json_encode( $data );
```

---

## 11. Database Queries

```php
global $wpdb;

// SELECT
$results = $wpdb->get_results( 
    $wpdb->prepare( 
        "SELECT * FROM {$wpdb->posts} WHERE post_type = %s", 
        'post' 
    ) 
);

// GET_ROW (un resultado)
$row = $wpdb->get_row( 
    $wpdb->prepare( 
        "SELECT * FROM {$wpdb->posts} WHERE ID = %d", 
        123 
    ) 
);

// GET_COL (una columna)
$ids = $wpdb->get_col( "SELECT ID FROM {$wpdb->posts}" );

// GET_VAR (un valor)
$count = $wpdb->get_var( "SELECT COUNT(*) FROM {$wpdb->posts}" );

// INSERT
$wpdb->insert( 
    'my_table', 
    [ 
        'name' => 'John',
        'email' => 'john@example.com' 
    ],
    [ '%s', '%s' ]
);

// UPDATE
$wpdb->update(
    'my_table',
    [ 'name' => 'Jane' ],
    [ 'id' => 1 ],
    [ '%s' ],
    [ '%d' ]
);

// DELETE
$wpdb->delete( 'my_table', [ 'id' => 1 ], [ '%d' ] );
```

---

## 12. Logging en WordPress

```php
// Habilitar logging
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );

// Escribir a wp-content/debug.log
error_log( 'My debug message' );
error_log( print_r( $data, true ) );

// Condicional
if ( WP_DEBUG ) {
    error_log( 'Debug only in development' );
}
```

---

## 13. REST API

```php
// Registrar endpoint
add_action( 'rest_api_init', 'my_plugin_register_rest_routes' );
function my_plugin_register_rest_routes() {
    register_rest_route(
        'my-plugin/v1',
        '/products',
        [
            'methods' => 'GET',
            'callback' => 'my_plugin_get_products',
            'permission_callback' => '__return_true'
        ]
    );
}

function my_plugin_get_products() {
    $products = wc_get_products( [ 'limit' => 10 ] );
    return rest_ensure_response( $products );
}
```

---

## 14. Gotchas Comunes

### wp_die() detiene ejecución

```php
if ( ! current_user_can( 'manage_options' ) ) {
    wp_die( 'No permission' );  // Detiene aquí
}
```

### Action vs Filter

```php
// Action: ejecuta código, no retorna nada
do_action( 'my_event' );

// Filter: transforma y retorna
$output = apply_filters( 'my_filter', $output );
```

### Escapar siempre output

```php
// MALO
echo $user_input;

// BIEN
echo esc_html( $user_input );
```

---

## 15. Recursos Oficiales

- [WordPress Plugin Developer Handbook](https://developer.wordpress.org/plugins/)
- [WordPress Hooks Reference](https://developer.wordpress.org/plugins/hooks/)
- [WooCommerce Developer Docs](https://woocommerce.com/document/woocommerce-rest-api/)
- [WordPress Coding Standards](https://developer.wordpress.org/coding-standards/)

