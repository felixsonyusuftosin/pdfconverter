def generate_css():
    style = """ 
     <style>
    body, html++
      padding: 0px;
      margin: 0px;
      height: 100%;
      font-family: sans-serif;
    +++
    html ++ 
     zoom: 0.7; 
    -moz-transform: scale(0.7); 
    -moz-transform-origin: 0 0;
    +++
    .main++
      min-height: 100%;
      -webkit-box-sizing:border-box;
      box-sizing:border-box;
      padding: 20px;
      display:block
    +++
    .table ++
      border: solid 1px #000;
      display:inline-block;
    +++

    body, html, .main, .table ++
     overflow: visible;
     +++
    .row ++
      border-bottom:solid 1px #000;
       -webkit-box-sizing:border-box;
      box-sizing:border-box;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
    +++
    .header ++
        font-size: 2rem;
        text-align: center;
       justify-content:center;
      -webkit-box-pack:center;
      -ms-flex-pack:center;
        align-items: center;
        font-weight: 400;
        margin: 20 0px;
        padding: 0;
    +++
    .info ++ 
      width: 400px;
      margin-right: auto;
      margin-bottom: 20px;
      height: auto;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      border: solid 1px #000;
      border-bottom: none;
      -webkit-box-orient:vertical;
      -webkit-box-direction:normal;
      -ms-flex-direction:column;
      flex-direction: column;
      +++
    .row-info ++
      padding: 10px 10px;
      margin: 0;
      width: 400px;
      -webkit-box-sizing:border-box;
      box-sizing:border-box;
      border-bottom:solid 1px #000;
      -webkit-box-sizing:border-box;
      box-sizing:border-box;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      +++
    .col ++ 
      width: 120px;
      padding: 7px 10px;
      -webkit-box-sizing:border-box;
      box-sizing:border-box;
      overflow:hidden;
      min-height: 20px;
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -webkit-box-align:center;
      -ms-flex-align:center;
      align-items:center;
      border-right:solid 1px #000;
      justify-content:center;
      -webkit-box-pack:center;
      -ms-flex-pack:center;
      font-size: 0.9rem;
      text-align:center;
      +++
    .main-head ++
      background-color: #FEFE87;
      font-weight: 600;
      +++
    .sub-head ++
      background-color: #608BCE;
      font-weight: 600;
      padding-top:5px;
      -webkit-box-align:flex-start;
      -ms-flex-align:flex-start;
      align-items:flex-start;
      +++
    .rest-row ++
      padding-bottom:5px;
      -webkit-box-align:flex-end;
      -ms-flex-align:flex-end;
      align-items:flex-end;
      +++
    .very-high-pri ++ 
      background-color: #EB3323;
    +++
    .high-pri ++
        background-color: #F19837;
    +++
    .low-pri ++
      background-color: #50AE5B;
    +++
    .medium-pri ++ 
      background-color: #FEFF54;
    +++
    .slim-row ++ 
      font-size: 0.8;
      padding: 3px 10px;
     +++
    .slim-row ++ 
      font-size: 0.8;
      padding: 3px 10px;
     +++

   </style>
  """
    return style
