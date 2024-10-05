from bubu import send_request

text_request = """Столбцы: Название офиса, Адрес офиса. 
БЦ «Красная Роза» - 119021, Москва, ул. Льва Толстого, 16. 
БЦ «Аврора» - 115035, Москва, ул. Садовническая, 82с2. 
БЦ «Око» - 123112, Москва, 1-й Красногвардейский проезд, 21с1, подъезд В. 
БЦ «Нева» - 123312, Москва, 1-й Красногвардейский проезд, 22с1. 
БЦ «Лотте Плаза» - 121099, Москва, Новинский бульвар, 8с1. 
Центр робототехники - 119501, Москва, ул. Лобачевского, 130Г."""

access_token = "t1.9euelZqdkZqXkpLNlMzKio_MlIrJje3rnpWazcrMxp7Pi4-KlJmMnJnInsvl8_cOFnpH-e8_WQk8_N3z905Ed0f57z9ZCTz8zef1656VmsyTjprHkYnHj4vPycfOls2N7_zF656VmsyTjprHkYnHj4vPycfOls2N.MpoMHI76kKiyhdCgqeKFabhM9B24kwJ1_fIO4U8lt1kK9hHIf4UMkDu4XtQF_sZLymGBbSdvutz9klSZ-NP7Cg"
catalog_id = "b1g0or8o57qjta3hncoe"

output_file = "bubu_output.csv"

send_request(text_request, access_token, catalog_id, output_file)
