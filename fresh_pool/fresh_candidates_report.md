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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CELESTARA-VLESS-WS-54MS` (url=251ms, nekobox=236ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-55MS` (url=213ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-53MS` (url=211ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-56MS` (url=218ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-52MS` (url=213ms, nekobox=237ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=210ms, nekobox=237ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-76MS` (url=215ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-74MS` (url=210ms, nekobox=238ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-100MS` (url=211ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=220ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-108MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-98MS` (url=215ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=218ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=211ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-56MS` (url=216ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-105MS` (url=220ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-68MS` (url=220ms, status=HTTP 204)
18. `AKUN-020-GOOGLE-VLESS-WS-70MS` (url=211ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-100MS` (url=224ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-127MS` (url=210ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-73MS` (url=212ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-59MS` (url=216ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-97MS` (url=350ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-342MS` (url=772ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-319MS` (url=689ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
