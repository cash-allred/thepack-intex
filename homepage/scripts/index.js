(function(context) {
    
    // utc_epoch comes from index.py
    console.log('Current epoch in UTC is ' + context.utc_epoch);
    
})(DMP_CONTEXT.get());

$(function() {
    // update the time every 1 seconds
    window.setInterval(function() {
        $('.browser-time').text('The current browser time is ' + new Date() + '.');
    }, 1000);
});

$(function(context) {
    return function() {
        console.log(context)
        var serverTime = new Date(context.now)   // server time (from DMP_CONTEXT)
        var browserTime = new Date()             // browser time
        var hours = Math.round(Math.abs(serverTime - browserTime) / 36e5)
        $('.browser-time').text('The current browser is ' + hours + ' hours off of the server time zone.')
    }
}(DMP_CONTEXT.get()))


$(function() {
    // update the time every n seconds
    window.setInterval(function() {
        $('.browser-time').text('The current browser time is ' + new Date());
    }, 1000);

    // update server time button
    $('#server-time-button').click(function() {
        $('.server-time').load('/homepage/index.gettime');
    });
});