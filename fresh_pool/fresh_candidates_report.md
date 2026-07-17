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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=228ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=224ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=236ms, nekobox=235ms, status=yes)
4. `AKUN-004-DIXONS-VLESS-WS-89MS` (url=218ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=203ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=198ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=223ms, nekobox=233ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-120MS` (url=246ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=207ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-124MS` (url=200ms, status=HTTP 204)
15. `AKUN-015-DIXONS-VLESS-WS-92MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-NEXUSMODS-VLESS-WS-103MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-WEBEX-VLESS-WS-93MS` (url=238ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-97MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-ORG-VLESS-WS-95MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-100MS` (url=232ms, status=HTTP 204)
21. `AKUN-021-SHOPIFY-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-1PASSWORD-VLESS-WS-130MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-POLICE-VLESS-WS-141MS` (url=242ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-244MS` (url=532ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-236MS` (url=504ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
