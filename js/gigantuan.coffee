$ ->
    $('#main section h1').each (index) ->
        $(this).wrapInner('<span class="slabtext" />')
    
    $('.slabtext').slabText
        viewportBreakpoint: '30em',
        headerBreakpoint: '30em'
