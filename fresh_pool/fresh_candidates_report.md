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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=228ms, nekobox=259ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-99MS` (url=216ms, nekobox=254ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-109MS` (url=219ms, nekobox=267ms, status=yes)
4. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS` (url=215ms, nekobox=184ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-112MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-366MS`
12. `AKUN-014-CLOUDFLARE-VLESS-WS-428MS` (url=805ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-403MS` (url=3099ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-389MS` (url=817ms, status=HTTP 204)
15. `AKUN-018-ARAD-VLESS-WS-549MS` (url=875ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-552MS` (url=985ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-628MS` (url=1030ms, status=HTTP 204)
18. `AKUN-027-CLOUDFLARE-VLESS-WS-446MS` (url=828ms, status=HTTP 204)
19. `AKUN-032-CLOUDFLARE-VLESS-WS-692MS` (url=1208ms, status=HTTP 204)
20. `AKUN-034-CLOUDFLARE-VLESS-WS-724MS` (url=1153ms, status=HTTP 204)
21. `AKUN-035-CLOUDFLARE-VLESS-WS-396MS` (url=820ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
