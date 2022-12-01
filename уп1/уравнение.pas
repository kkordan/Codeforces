var a,b,n,m,s:integer;
begin
  read (n,m);
 
 s:=0;
 for a:=0 to 1000 do
  begin
  for b:=0 to 1000 do
     if (sqr(a)+ b=n) and (a+sqr(b)=m) then
       s:=s+1;
     end;
   write (s)
   end.