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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=232ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=212ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=204ms, nekobox=276ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=213ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=197ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, nekobox=229ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-98MS` (url=231ms, nekobox=239ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-96MS` (url=212ms, nekobox=245ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-86MS` (url=224ms, nekobox=265ms, status=yes)
10. `AKUN-010-OVH-VLESS-WS-102MS` (url=252ms, nekobox=250ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-111MS` (url=214ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-99MS` (url=201ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-96MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-77MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-130MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-142MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-110MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-140MS` (url=221ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-90MS` (url=234ms, status=HTTP 204)
20. `AKUN-020-WEBEX-VLESS-WS-114MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-229MS` (url=498ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-241MS` (url=482ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-124MS` (url=218ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-224MS` (url=527ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-268MS` (url=593ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
