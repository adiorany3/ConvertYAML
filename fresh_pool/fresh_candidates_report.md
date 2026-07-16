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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=221ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=245ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=259ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=264ms, nekobox=276ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-102MS` (url=263ms, nekobox=325ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-103MS` (url=272ms, nekobox=307ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-103MS` (url=238ms, nekobox=266ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=273ms, nekobox=289ms, status=yes)
9. `AKUN-009-NEXUSMODS-VLESS-WS-109MS` (url=336ms, nekobox=347ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-91MS` (url=258ms, nekobox=274ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-112MS` (url=365ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=250ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-104MS` (url=266ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-120MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-142MS` (url=273ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=286ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-143MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-148MS` (url=273ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-141MS` (url=254ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-166MS` (url=434ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-109MS` (url=398ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-103MS` (url=249ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-186MS` (url=255ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-170MS` (url=244ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
