% rebase('layout.tpl', title=title)

<html>
<div class="jumbotron">
<style>
 h2{
  font-size: 200%;
  font-family: Verdana, Arial, Helvetica, sans-serif;
  color: #333366;
 }
 .test {

 display: inline;
 margin-right: 55%;
 }
 }
</style>
 <head>
  <h2 align = center>{{ title }}</h2>
 
  <form action = "/Dextra" method="post">
     <p align=center>{{title_size}}</p>
      <style>
       select{width: 150px;}
      </style>
       <p align=center><select name = "GetValue"  id="val">
      <option selected  value = 4> 4 </option>
      <option  value = 5> 5 </option>
      <option  value = 6> 6 </option>
      <option  value = 7> 7 </option>
      <option  value = 8> 8 </option>
      <option  value = 9> 9 </option>
      </select></p>

       <style>
       textarea {
        width: 500px; 
        height: 40px; 
        resize: none;
        top: 50%;

       } 
      </style>
       <style>
       .outline {
        border:3px #00B344 
        solid; width:300px;
        margin: auto;
       }
      </style>
       <div class="outline">
       <p align=center>{{text_info}}</p>
       <p> x4: A, B, C, D </p>
       <p> x5: A, B, C, D, E </p>
       <p> x6: A, B, C, D, E, F </p>
       <p> x7: A, B, C, D, E, F, G </p>
       <p> x8: A, B, C, D, E, F, G, H </p>
       <p> x9: A, B, C, D, E, F, G, H, I </p>
      </div>

      <p align=center><textarea placeholder = {{text_litr}} name="Litr"  maxlength = "1" rows = "1" cols = "40"></textarea></p>
     <style>
            .button {
            border-radius: 12px;
            background: wight;
            border-color: #cccccc;
            color: white;
            padding: 15px 45px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            position: relative;
            left: 50%;
            transform: translate(-50%,0);
            margin: 5% auto;
            cursor: pointer;
            }
            .button1{background-color: #4CAF50;}
     </style>
        <button class="button button1">{{title_enter}}</button>
</form>
</div>
</html>
