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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=216ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=213ms, nekobox=247ms, status=yes)
3. `AKUN-003-XTOM-KIX-VLESS-WS-66MS` (url=211ms, nekobox=251ms, status=yes)
4. `AKUN-004-DE-XTOM-20190821-VLESS-WS-63MS` (url=226ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=222ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=218ms, nekobox=247ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-89MS` (url=250ms, nekobox=250ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-96MS` (url=227ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS` (url=227ms, nekobox=252ms, status=yes)
10. `AKUN-010-NODEHOST-VLESS-WS-78MS` (url=241ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-64MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-72MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-PUBLICDOMAINREGISTRY-NET-VLESS-WS-103MS` (url=287ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-76MS` (url=212ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-93MS` (url=227ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-112MS` (url=222ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-174MS` (url=344ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=239ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-342MS` (url=740ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-362MS` (url=4994ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-447MS` (url=1027ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-704MS` (url=1131ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-710MS` (url=1104ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
