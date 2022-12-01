var a,b,c,d:integer;
begin
  readln(a,b);
  c:=a*b;
  
  if c mod 2 =0 then 
    write (c div 2)
  else
    write ((c-1)div 2);
end.