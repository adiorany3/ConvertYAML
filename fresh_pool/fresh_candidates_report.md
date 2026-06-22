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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-128MS` (url=247ms, nekobox=273ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-110MS` (url=269ms, nekobox=323ms, status=yes)
3. `AKUN-003-DIGITALOCEAN-VLESS-WS-123MS` (url=254ms, nekobox=290ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-129MS` (url=263ms, nekobox=289ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-117MS` (url=324ms, nekobox=225ms, status=no)
6. `AKUN-005-008500-VLESS-WS-132MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-133MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-139MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-152MS`
10. `AKUN-009-US-VLESS-WS-122MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-156MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-142MS` (url=264ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-142MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-152MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-136MS` (url=367ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-180MS` (url=256ms, status=HTTP 204)
18. `AKUN-018-1PASSWORD-VLESS-WS-115MS` (url=251ms, status=HTTP 204)
19. `AKUN-019-ADF-VLESS-WS-116MS` (url=316ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=358ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-330MS` (url=763ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-329MS` (url=601ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-361MS` (url=726ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-359MS` (url=682ms, status=HTTP 204)
25. `AKUN-026-DIGITALOCEAN-VLESS-WS-125MS` (url=348ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
