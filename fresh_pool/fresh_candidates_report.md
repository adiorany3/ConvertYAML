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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=224ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=227ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, nekobox=237ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-81MS` (url=230ms, nekobox=225ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=211ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=260ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=218ms, nekobox=243ms, status=yes)
8. `AKUN-008-MGN-20250528-VLESS-WS-100MS` (url=225ms, nekobox=263ms, status=yes)
9. `AKUN-009-CZ-LOTUNA-19970206-VLESS-WS-103MS` (url=225ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-129MS` (url=228ms, nekobox=253ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-74MS` (url=240ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-130MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-95MS` (url=196ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-140MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-64MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-151MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-187MS` (url=331ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-90MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-96MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-113MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-167MS` (url=225ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-91MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-225MS` (url=993ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-240MS` (url=294ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-236MS` (url=524ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
