% rebase('layout.tpl', title='Home Page')

<div class="jumbotron">
<img src="static\image\1.png" align ="left">
      <h1>Calculator</h1>
        <p>{{title1}}</p>
        <p>{{title2}}</p>
</div>
<div>
        <style>
        .h4 {
        border-radius: 12px;
        background: wight;
        border-color: #cccccc;
        color: black;
        font-size: 9pt;
        height: 70px;
        width: 200px;
        position: relative;
        left: 50%;
        transform: translate(-50%,0);
        }

        </style>
        <p><a href=/Main><input type=button class=h4  value={{btn_text}}></a></p>
</div>