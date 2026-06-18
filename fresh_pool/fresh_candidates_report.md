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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-103MS` (url=285ms, nekobox=311ms, status=yes)
2. `AKUN-002-1PASSWORD-VLESS-WS-106MS` (url=243ms, nekobox=297ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-125MS` (url=297ms, nekobox=301ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-101MS` (url=320ms, nekobox=335ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-132MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS` (url=269ms, nekobox=247ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-143MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-170MS` (url=235ms, nekobox=212ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS`
11. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-126MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-163MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-137MS` (url=288ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-171MS` (url=289ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-340MS` (url=615ms, status=HTTP 204)
16. `AKUN-018-WPENG-VLESS-WS-366MS` (url=711ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-371MS` (url=2703ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-351MS` (url=752ms, status=HTTP 204)
19. `AKUN-022-CONFLU-VLESS-WS-313MS` (url=611ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-116MS` (url=272ms, status=HTTP 204)
21. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-398MS` (url=728ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-385MS` (url=475ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-106MS` (url=334ms, status=HTTP 204)
24. `AKUN-033-ONTHEWIFI-VLESS-WS-602MS` (url=1502ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-844MS` (url=1354ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
