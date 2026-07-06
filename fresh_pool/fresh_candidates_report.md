# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-90MS` (url=238ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=209ms, nekobox=240ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-103MS` (url=271ms, nekobox=282ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-116MS` (url=237ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-111MS` (url=204ms, nekobox=184ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-76MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-126MS`
10. `AKUN-009-WPENG-VLESS-WS-69MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-222MS` (url=3535ms, nekobox=7176ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-249MS`
13. `AKUN-016-CLOUDFLARE-VLESS-WS-255MS` (url=1032ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-290MS` (url=589ms, status=HTTP 204)
15. `AKUN-018-GALAKTIKA-20201015-VLESS-WS-283MS` (url=607ms, status=HTTP 204)
16. `AKUN-019-WPENG-VLESS-WS-295MS` (url=592ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-276MS` (url=527ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-267MS` (url=809ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-423MS` (url=750ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-452MS` (url=800ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-553MS` (url=995ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
