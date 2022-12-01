var
  a, i,s: integer;

begin
  readln(a);
  s:=0;
  if a=1 then
  begin
  write('I hate it');
  exit;
  end
  else
   repeat
    s:=s+1;
    if s mod 2=0 then
      
       begin
       write ('I love');
     end
     else
      begin
      write ('I hate');
     end;
     if s<=a-1 then
     write (' that ');
     
   until s=a;
   write (' it');
end.