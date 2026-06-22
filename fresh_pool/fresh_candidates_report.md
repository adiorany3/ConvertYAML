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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=211ms, nekobox=242ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=231ms, nekobox=265ms, status=yes)
3. `AKUN-003-PUBLICDOMAINREGISTRY-NET-VLESS-WS-106MS` (url=222ms, nekobox=248ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS` (url=280ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=214ms, nekobox=271ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-122MS` (url=204ms, nekobox=272ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=202ms, nekobox=253ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-142MS` (url=208ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-140MS` (url=209ms, nekobox=242ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=212ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-152MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-264MS` (url=574ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-247MS` (url=505ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-254MS` (url=516ms, status=HTTP 204)
15. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-295MS` (url=583ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-287MS` (url=567ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-311MS` (url=602ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-324MS` (url=627ms, status=HTTP 204)
19. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-509MS` (url=844ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-101MS` (url=231ms, status=HTTP 204)
21. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-494MS` (url=707ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-147MS` (url=224ms, status=HTTP 204)
23. `AKUN-030-UK-GB-DCL-01-20191003-VLESS-WS-597MS` (url=2545ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-597MS` (url=985ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
