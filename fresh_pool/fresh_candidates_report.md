# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-VULTR-VLESS-WS-130MS` (url=257ms, nekobox=269ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-125MS` (url=308ms, nekobox=281ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-101MS` (url=299ms, nekobox=307ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=282ms, nekobox=317ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS` (url=272ms, nekobox=304ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=292ms, nekobox=308ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS` (url=317ms, nekobox=325ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS` (url=257ms, nekobox=306ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-171MS` (url=274ms, nekobox=313ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-273MS` (url=559ms, nekobox=465ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-289MS` (url=568ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-308MS` (url=722ms, status=HTTP 204)
13. `AKUN-014-WPENG-VLESS-WS-348MS` (url=776ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-356MS` (url=667ms, status=HTTP 204)
15. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-339MS` (url=753ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-328MS` (url=630ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-363MS` (url=708ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-354MS` (url=757ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-399MS` (url=580ms, status=HTTP 204)
20. `AKUN-034-CLOUDFLARE-VLESS-WS-613MS` (url=1039ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
