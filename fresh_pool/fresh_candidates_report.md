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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=230ms, nekobox=204ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=205ms, nekobox=181ms, status=no)
6. `AKUN-004-DEV-VLESS-WS-90MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS`
9. `AKUN-007-1PASSWORD-VLESS-WS-107MS`
10. `AKUN-008-MYBB-VLESS-WS-84MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS`
12. `AKUN-010-MEDIUM-VLESS-WS-88MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-119MS` (url=226ms, status=HTTP 204)
16. `AKUN-016-OVH-VLESS-WS-89MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-NET-82-21-84-0-24-VLESS-WS-130MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
20. `AKUN-020-OVH-VLESS-WS-88MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-100MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-110MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-108MS` (url=204ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-92MS` (url=261ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-243MS` (url=499ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
