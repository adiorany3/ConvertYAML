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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=243ms, nekobox=283ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=249ms, nekobox=180ms, status=no)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=262ms, nekobox=180ms, status=no)
4. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-76MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=278ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-184MS` (url=418ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=249ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-276MS` (url=560ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-76MS` (url=240ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-294MS` (url=654ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-73MS` (url=254ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-287MS` (url=675ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-287MS` (url=636ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-305MS` (url=663ms, status=HTTP 204)
25. `AKUN-027-BROADNNET-KR-VLESS-WS-334MS` (url=703ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
