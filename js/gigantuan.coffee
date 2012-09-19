$ ->
    $.jqwidont.auto(false);
    $('#main section h1').each ->
        $(this).fitText(1.5);
        $.jqwidont.init();
    
    $('.slabtext').slabText
        viewportBreakpoint: '25em',
        headerBreakpoint: '25em'
