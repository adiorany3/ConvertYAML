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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=317ms, nekobox=312ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS`
3. `AKUN-003-UNKNOWN-VLESS-WS-94MS`
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-111MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-128MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-107MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-107MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=334ms, status=HTTP 204)
12. `AKUN-014-UNKNOWN-VLESS-WS-130MS` (url=328ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-135MS` (url=282ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-159MS` (url=318ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-228MS` (url=501ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-200MS` (url=436ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-213MS` (url=437ms, status=HTTP 204)
18. `AKUN-020-GALAKTIKA-20201015-VLESS-WS-300MS` (url=608ms, status=HTTP 204)
19. `AKUN-021-LEVIKOGJGFDD-VLESS-WS-298MS` (url=831ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-151MS` (url=499ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-323MS` (url=688ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-195MS` (url=447ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-404MS` (url=531ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-519MS` (url=1139ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-573MS` (url=951ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
