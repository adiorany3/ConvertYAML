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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=216ms, nekobox=232ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=203ms, nekobox=241ms, status=yes)
3. `AKUN-003-SAVVY-7-VLESS-WS-69MS` (url=211ms, nekobox=250ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=206ms, nekobox=246ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-68MS` (url=214ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=199ms, nekobox=230ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=210ms, nekobox=229ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS` (url=207ms, nekobox=231ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS` (url=199ms, nekobox=237ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS` (url=210ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-106MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-72MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-87MS` (url=194ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-71MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-68MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-136MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-137MS` (url=199ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-110MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-DIXONS-VLESS-WS-119MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-74MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-110MS` (url=227ms, status=HTTP 204)
23. `AKUN-023-UK-GB-DCL-01-20191003-VLESS-WS-153MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-150MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-224MS` (url=506ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
