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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=198ms, nekobox=229ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-62MS` (url=207ms, nekobox=228ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-67MS` (url=202ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=218ms, nekobox=248ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=202ms, nekobox=231ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-66MS` (url=207ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=211ms, nekobox=235ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-67MS` (url=219ms, nekobox=252ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-71MS` (url=209ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-69MS` (url=224ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-65MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-EE-WELCOMEHOST-20190515-VLESS-WS-77MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=514ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-87MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-79MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDWEBMANAGE-EU-FR-VLESS-WS-92MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-66MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-76MS` (url=225ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-78MS` (url=206ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-89MS` (url=222ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-89MS` (url=197ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-148MS` (url=291ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
