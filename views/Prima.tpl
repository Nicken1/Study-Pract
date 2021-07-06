% rebase('layout.tpl', title=title)

<html>
<div class="jumbotron">
<style>
 h2{
  font-size: 200%;
  font-family: Verdana, Arial, Helvetica, sans-serif;
  color: #333366;
 }
</style>
<head>
  <h2 align = center>{{ title }}</h2>
</head>
<form action = "/Prima" method="post">
     <p align=center>{{title_size}}</p>
      <style>
       select{width: 150px;}
      </style>
     <p align=center>
         <select name = "GetValue">
          <option value = 4> 4 </option>
          <option value = 5> 5 </option>
          <option value = 6> 6 </option>
          <option value = 7> 7 </option>
          <option value = 8> 8 </option>
          <option value = 9> 9 </option>
         </select>
     </p>
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
