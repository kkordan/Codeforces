var
  n, k, i, i2, s,i3: integer;
  a: array[1..50] of integer;

begin
  s := 0;
  read(n, k);
  for i := 1 to n do
  begin
    read(a[i]);
  end;
  
 
  for i2 := 1 to n do
  begin
    
    if (a[i2] >= a[k]) and (a[i2]<>0) then
 
    begin
      s := s + 1;
    end;
  end;
  write(s);
end.