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
1. `AKUN-001-OVH-VLESS-WS-61MS` (url=211ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=213ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=212ms, nekobox=242ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-99MS` (url=222ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=214ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-104MS` (url=212ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-65MS` (url=226ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=212ms, nekobox=227ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-86MS` (url=203ms, nekobox=262ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, nekobox=237ms, status=yes)
11. `AKUN-011-GOOGLE-VLESS-WS-127MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-59MS` (url=212ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-104MS` (url=300ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-347MS` (url=768ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-327MS` (url=608ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-500MS` (url=992ms, status=HTTP 204)
17. `AKUN-018-SPEEDTEST-VLESS-WS-57MS` (url=666ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-519MS` (url=993ms, status=HTTP 204)
19. `AKUN-020-SUKARIO-VLESS-WS-592MS` (url=972ms, status=HTTP 204)
20. `AKUN-021-HCAPTCHA-VLESS-WS-608MS` (url=903ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-612MS` (url=1016ms, status=HTTP 204)
22. `AKUN-023-SPEEDTEST-VLESS-WS-695MS` (url=693ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-686MS` (url=1050ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-643MS` (url=981ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-700MS` (url=1168ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
