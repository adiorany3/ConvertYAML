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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=215ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=209ms, nekobox=241ms, status=yes)
3. `AKUN-003-LT-LRTC-20060503-VLESS-WS-74MS` (url=215ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=210ms, nekobox=227ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-79MS` (url=203ms, nekobox=196ms, status=no)
6. `AKUN-005-ZVC-VLESS-WS-90MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=222ms, nekobox=199ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, nekobox=207ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
11. `AKUN-008-WPENG-VLESS-WS-88MS`
12. `AKUN-009-GALAKTIKA-20201015-VLESS-WS-76MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-PAGES-VLESS-WS-79MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-103MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-95MS` (url=292ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-91MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-110MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-111MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-78MS` (url=213ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-228MS` (url=521ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-237MS` (url=528ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-263MS` (url=317ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
