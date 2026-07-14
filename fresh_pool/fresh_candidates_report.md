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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=219ms, nekobox=252ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-83MS` (url=231ms, nekobox=230ms, status=yes)
3. `AKUN-003-UBI-VLESS-WS-80MS` (url=218ms, nekobox=228ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-92MS` (url=210ms, nekobox=262ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-87MS` (url=207ms, nekobox=262ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-95MS` (url=221ms, nekobox=199ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
8. `AKUN-007-ZVC-VLESS-WS-101MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-102MS` (url=218ms, nekobox=7176ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=255ms, nekobox=213ms, status=no)
11. `AKUN-008-466688-VLESS-WS-111MS`
12. `AKUN-012-DEV-VLESS-WS-105MS` (url=216ms, nekobox=224ms, status=no)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-106MS` (url=223ms, nekobox=213ms, status=no)
14. `AKUN-009-UNKNOWN-VLESS-WS-109MS`
15. `AKUN-010-WPENG-VLESS-WS-99MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-94MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=852ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-142MS` (url=268ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-136MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-116MS` (url=214ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-236MS` (url=520ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-240MS` (url=509ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-258MS` (url=518ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
