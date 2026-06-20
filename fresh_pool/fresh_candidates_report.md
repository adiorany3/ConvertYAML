# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS` (url=261ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS` (url=231ms, nekobox=218ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-244MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS` (url=235ms, nekobox=201ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-303MS` (url=2602ms, nekobox=412ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=212ms, nekobox=205ms, status=no)
12. `AKUN-008-CLOUDFLARE-VLESS-WS-100MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-391MS` (url=589ms, nekobox=497ms, status=no)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-386MS` (url=603ms, nekobox=528ms, status=no)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-397MS` (url=557ms, nekobox=484ms, status=no)
17. `AKUN-010-US-VLESS-WS-153MS`
18. `AKUN-018-CLOUDFLARE-VLESS-WS-391MS` (url=629ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-387MS` (url=613ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-89MS` (url=206ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-404MS` (url=598ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-95MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-403MS` (url=640ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-379MS` (url=579ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-417MS` (url=617ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
