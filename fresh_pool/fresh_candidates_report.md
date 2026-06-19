# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-100MS` (url=231ms, nekobox=283ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-109MS` (url=207ms, nekobox=261ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-113MS` (url=277ms, nekobox=243ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-114MS` (url=234ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-127MS` (url=207ms, nekobox=263ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=200ms, nekobox=191ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-137MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-247MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-262MS` (url=573ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-276MS` (url=4767ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-242MS` (url=540ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-277MS` (url=603ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-267MS` (url=571ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-292MS` (url=4451ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-316MS` (url=2852ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-337MS` (url=558ms, status=HTTP 204)
20. `AKUN-026-CLOUDFLARE-VLESS-WS-393MS` (url=581ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-384MS` (url=584ms, status=HTTP 204)
22. `AKUN-028-UNKNOWN-VLESS-WS-439MS` (url=644ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-459MS` (url=582ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
