var k,w,a,s:integer;
n:int64;
begin
  readln(k,n,w);
 s:=0;
 for a:=1 to w do
  begin
  s:= s + (a*k);
  end;
  if s<=n then 
    write ('0')
  else
    write (s-n);
end.