# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-ALIBABA-VLESS-WS-84MS` (url=228ms, nekobox=226ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-83MS` (url=234ms, nekobox=263ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=225ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-129MS` (url=200ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-120MS` (url=207ms, nekobox=265ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS` (url=235ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-119MS` (url=225ms, nekobox=246ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=233ms, nekobox=236ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=202ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-201MS` (url=432ms, nekobox=421ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-279MS` (url=602ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-300MS` (url=641ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-253MS` (url=528ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-321MS` (url=2294ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-324MS` (url=2289ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-296MS` (url=615ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-293MS` (url=593ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-252MS` (url=283ms, status=HTTP 204)
19. `AKUN-020-JISON-VLESS-WS-355MS` (url=679ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-460MS` (url=762ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-387MS` (url=497ms, status=HTTP 204)
22. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-517MS` (url=862ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-551MS` (url=893ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-689MS` (url=1618ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
