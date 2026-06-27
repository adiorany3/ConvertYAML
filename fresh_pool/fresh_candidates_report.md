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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=214ms, nekobox=231ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-106MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-113MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=235ms, nekobox=217ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=250ms, nekobox=202ms, status=no)
8. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS`
9. `AKUN-006-US-VLESS-WS-116MS`
10. `AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-126MS`
11. `AKUN-008-DIGITALOCEAN-VLESS-WS-125MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-140MS`
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-130MS` (url=313ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-156MS` (url=279ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-149MS` (url=291ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-119MS` (url=263ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-163MS` (url=285ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-122MS` (url=248ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-142MS` (url=223ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-143MS` (url=238ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-161MS` (url=429ms, status=HTTP 204)
25. `AKUN-025-CONFLU-VLESS-WS-394MS` (url=760ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
