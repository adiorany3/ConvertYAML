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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=360ms, nekobox=333ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-81MS` (url=291ms, nekobox=312ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=280ms, nekobox=377ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-87MS` (url=294ms, nekobox=341ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-89MS` (url=481ms, nekobox=325ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-108MS` (url=315ms, nekobox=304ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-110MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-86MS` (url=288ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-79MS` (url=281ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=295ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-136MS` (url=367ms, status=HTTP 204)
15. `AKUN-017-EU-VLESS-WS-130MS` (url=284ms, status=HTTP 204)
16. `AKUN-018-ZVC-VLESS-WS-83MS` (url=297ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-109MS` (url=347ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-108MS` (url=320ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-149MS` (url=294ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-148MS` (url=302ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-231MS` (url=467ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-312MS` (url=635ms, status=HTTP 204)
23. `AKUN-026-NET-141-11-202-0-23-VLESS-WS-315MS` (url=670ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-309MS` (url=504ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-576MS` (url=992ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
