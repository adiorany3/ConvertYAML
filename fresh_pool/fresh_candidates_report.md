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
1. `AKUN-001-UNKNOWN-VLESS-WS-100MS` (url=257ms, nekobox=360ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS` (url=330ms, nekobox=279ms, status=yes)
3. `AKUN-004-CLOUDFLARE-VLESS-WS-127MS` (url=244ms, nekobox=230ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-126MS`
5. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS` (url=240ms, nekobox=211ms, status=no)
6. `AKUN-004-UNKNOWN-VLESS-WS-143MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-155MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-165MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-140MS`
10. `AKUN-013-CLOUDFLARE-VLESS-WS-167MS` (url=318ms, nekobox=213ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-162MS`
12. `AKUN-015-CLOUDFLARE-VLESS-WS-154MS` (url=246ms, nekobox=208ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-134MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS`
15. `AKUN-018-US-VLESS-WS-114MS` (url=265ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-328MS` (url=695ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-325MS` (url=586ms, status=HTTP 204)
18. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-348MS` (url=758ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-363MS` (url=593ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-361MS` (url=724ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-349MS` (url=734ms, status=HTTP 204)
22. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-374MS` (url=747ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-570MS` (url=779ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-657MS` (url=1150ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-609MS` (url=965ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
