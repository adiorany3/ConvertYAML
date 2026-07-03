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
1. `AKUN-001-COMPREND-NET-VLESS-WS-74MS` (url=233ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-95MS` (url=210ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=237ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=240ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=243ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=223ms, nekobox=228ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=207ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=233ms, nekobox=234ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-101MS` (url=229ms, nekobox=255ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-85MS` (url=204ms, nekobox=255ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-113MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-107MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-104MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-104MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-112MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-117MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-PAGES-VLESS-WS-127MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-111MS` (url=201ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-85MS` (url=228ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-95MS` (url=262ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-368MS` (url=867ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-378MS` (url=798ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-390MS` (url=888ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
