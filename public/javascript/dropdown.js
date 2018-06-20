function initiate_dropdown() {
    $('#name_drop').dropdown({maxSelections: 10, apiSettings: {
      url: '/classnames'
    }})
}