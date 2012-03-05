Login form:

% if error:
    ${error}
% endif

<form method="POST" name="login" action="/login/save">
    <input type="text" name="login"><br/>
    <input type="password" name="password"><br/>
    <input type="submit" value="login">
</form>
