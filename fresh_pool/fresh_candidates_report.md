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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=270ms, nekobox=255ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-103MS` (url=267ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS` (url=282ms, nekobox=257ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-103MS` (url=223ms, nekobox=258ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-100MS` (url=217ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-108MS` (url=263ms, nekobox=315ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-112MS` (url=307ms, nekobox=280ms, status=yes)
8. `AKUN-008-US-VLESS-WS-111MS` (url=262ms, nekobox=219ms, status=no)
9. `AKUN-008-466688-VLESS-WS-110MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-138MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS`
12. `AKUN-012-MEDIUM-VLESS-WS-141MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-114MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-142MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-132MS` (url=243ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-131MS` (url=261ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-106MS` (url=362ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-121MS` (url=244ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-152MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-338MS` (url=589ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-382MS` (url=790ms, status=HTTP 204)
22. `AKUN-022-OCTOPUSSS5-VLESS-WS-392MS` (url=844ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-417MS` (url=802ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-399MS` (url=830ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-416MS` (url=859ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
