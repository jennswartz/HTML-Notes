def generate_concept_html(main_heading, subhead_description):
    html_text_1 = '''
<div class="main-heading">
    <div class="concept-title">
        ''' + main_heading
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + subhead_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_html(main):
    main_heading = main[0]
    subhead_description = main[1]
    return generate_concept_html(main_heading, subhead_description)

list_of_concepts = [ ['HTML', 'HTML is the basis for all web pages.  It provides the structure for webpages.'],
                    ['CSS', 'CSS means Cascading Style Sheets.  It adds style to a webpage.'],
                    ['Programming', 'A computer can be programmed to do anything we want.'], 
                    ['Variables and Strings', 'Variables are a value that can change, and a string is a sequence of characters.'],
                    ['Input-Function-Output', 'Computers need an input, then perform a function, then produce an output.'] ]


def make_html_for_many_concepts(list_of_concepts):
    html = ""
    for concept in list_of_concepts:
        concept_html = make_html(concept)
        html = html + concept_html
    return html

print make_html_for_many_concepts(list_of_concepts)
