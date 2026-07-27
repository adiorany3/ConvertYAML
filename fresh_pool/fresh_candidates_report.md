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
1. `AKUN-001-UNKNOWN-VLESS-WS-55MS` (url=215ms, nekobox=236ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=209ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=212ms, nekobox=243ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-82MS` (url=210ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=209ms, nekobox=235ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-72MS` (url=216ms, nekobox=233ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-89MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-74MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-63MS` (url=211ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-69MS` (url=235ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-55MS` (url=211ms, status=HTTP 204)
14. `AKUN-016-SKK-VLESS-WS-118MS` (url=415ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-116MS` (url=217ms, status=HTTP 204)
16. `AKUN-018-DEV-VLESS-WS-105MS` (url=859ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-349MS` (url=739ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-342MS` (url=2075ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-350MS` (url=842ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-118MS` (url=240ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-631MS` (url=1144ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-623MS` (url=979ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-625MS` (url=964ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-629MS` (url=1475ms, status=HTTP 204)
25. `AKUN-033-SPEEDTEST-VLESS-WS-770MS` (url=1059ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
