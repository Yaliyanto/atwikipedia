class LoginLocator :
    input_email = "username" #ID

    input_password = "password" #ID

    click_tick_box_term_condition = "agreeTnc" #ID

    click_button_agree_term_condition = value='id("modal-checklist-login")/div[@class="modal-dialog modal-lg"]/div[@class="modal-content"]/div[@class="modal-footer"]/button[@class="btn btn-primary form-control"]' #xpath

    click_tick_box_privacy_policy = value="/html/body/div[2]/div/div[1]/div[1]/div/form/div[4]/div[2]/input" #xpath

    click_button_agree_privacy_policy = value= "/html/body/div[2]/div/div[3]/div/div/div/div[3]/button" #xpath

    click_button_login = value="/html/body/div[2]/div/div[1]/div[1]/div/form/div[5]/button" #Xpath

    allert_user_account_not_found = 'id("toast-container")/div[@class="toast toast-warning"]' #Xpath (teks = User account not found)

    allert_incorrect_userORpassword = 'id("toast-container")/div[@class="toast toast-warning"]' #Xpath(teks = Incorrect user / password)

    teks_dashboard_hi_john_wick = 'id("app")/div[@class="layout-main"]/div[@class="layout-content"]/div[@class="layout-content-body"]/div[@class="dashboard-content"]/div[@class="row"]/div[@class="col-md-6"]/div[@class="title-bar-user"]/span[@class="title-bar-user-title"]'

    teks_berikut_aktivitas_anda_hari_ini = 'id("app")/div[@class="layout-main"]/div[@class="layout-content"]/div[@class="layout-content-body"]/div[@class="dashboard-content"]/div[@class="row"]/div[@class="col-md-6"]/div[@class="title-bar-user"]/p[@class="title-bar-user-description text-task"]/small[1]'
    