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
1. `AKUN-001-OVH-VLESS-WS-89MS` (url=249ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=209ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-87MS` (url=205ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-89MS` (url=206ms, nekobox=236ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=214ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS` (url=204ms, nekobox=240ms, status=yes)
7. `AKUN-007-DIXONS-VLESS-WS-100MS` (url=223ms, nekobox=245ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-104MS` (url=209ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=209ms, nekobox=256ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-92MS` (url=216ms, nekobox=248ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-111MS` (url=252ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-93MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-105MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-ORG-VLESS-WS-116MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-93MS` (url=314ms, status=HTTP 204)
16. `AKUN-016-VOV-VLESS-WS-96MS` (url=254ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-109MS` (url=303ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-109MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-120MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-111MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-127MS` (url=274ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-145MS` (url=266ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-161MS` (url=299ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-152MS` (url=224ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-200MS` (url=288ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
