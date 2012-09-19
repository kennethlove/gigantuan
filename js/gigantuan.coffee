$ ->
    $('#main section h1').each ->
        $(this).wrapInner('<span class="slabtext" />')
    
    $('.slabtext').slabText
        viewportBreakpoint: '25em',
        headerBreakpoint: '25em'
