from dash import html, dcc
import dash_bootstrap_components as dbc
from json import dumps

container = html.Div(id='container', className='container')

col1 = dbc.Accordion(class_name='col-4',start_collapsed=True,
                     children=[dbc.AccordionItem(title="label",
                                                 children=[dcc.Input(id='label_text', className='col-12', placeholder='label text_value'),
                                                           dcc.Input(id='label_size', className='col-12', placeholder='label font_size'),
                                                           dcc.Input(id='label_color', className='col-12', placeholder='label font_color in hex #000000 - #FFFFFF'),
                                                           html.Button(id='label_btn', className='col-12 btn btn-outline-primary', children='Add Label')
                                                           ],
                                                 ),
                               dbc.AccordionItem(title="button",
                                                 children=[dcc.Input(id='title_text', className='col-12', placeholder='title text_value'),
                                                           dcc.Input(id='title_size', className='col-12', placeholder='title font_size'),
                                                           dcc.Input(id='title_color', className='col-12', placeholder='title font_color in hex #000000 - #FFFFFF'),
                                                           html.Button(id='title_btn', className='col-12 btn btn-outline-primary', children='Add Button')
                                                           ],
                                                 ),
                               dbc.AccordionItem(title="vlist",
                                                 children="This is feature is under development"
                                                 ),
                               dbc.AccordionItem(title="hlist",
                                                 children="This is feature is under development",

                                                 )
                               ])

col2 = html.Div(id='json_response', className='col-8', children=dumps({'components': []}))

row0 = html.Button(id='undo_btn', className='col-4 btn btn-outline-primary', children='Remove Last Added component')

row1 = html.Div(id='row1', className='row', children=[col1, col2])
 
row_email = html.Div(id='row_email', className='row',
                children=[dcc.Input(id='username', className='col-4', placeholder='Enter Email')])
row_passwd = html.Div(id='row_passwd', className='row',
                children=[dcc.Input(id='password', className='col-4', placeholder='Enter Password',type='password')])
                          
row3 = html.Div(id='row3', className='row',
                children = html.Button(id='load_json', className='col-4 btn btn-outline-primary', children='Load JSON From database'))
row4 = html.Div(id='row4', className='row',
                children = html.Button(id='store_json', className='col-4 btn btn-outline-primary', children='Store JSON In database'))

row5 = html.Div(id='database_response')
row6 = html.Div(id='serving_at',children='Json components are being served at e.g. http://apixcodefordevelopers.ml:5000/?username=bhooshan&password=patil')
container.children = [row0, row1, row_email,row_passwd, row3,row4,row5,row6]
