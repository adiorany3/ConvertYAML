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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-110MS` (url=276ms, nekobox=280ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-114MS` (url=281ms, nekobox=286ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-134MS` (url=255ms, nekobox=399ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-121MS` (url=330ms, nekobox=294ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-137MS` (url=290ms, nekobox=346ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-144MS` (url=302ms, nekobox=324ms, status=yes)
7. `AKUN-007-ZOOM-VLESS-WS-128MS` (url=335ms, nekobox=379ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-126MS` (url=284ms, nekobox=343ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-137MS` (url=318ms, nekobox=311ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-154MS` (url=324ms, nekobox=387ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-128MS` (url=306ms, status=HTTP 204)
12. `AKUN-012-DIGITALOCEAN-VLESS-WS-117MS` (url=312ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=347ms, status=HTTP 204)
14. `AKUN-014-AEZA-NETWORK-VLESS-WS-130MS` (url=303ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-137MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-133MS` (url=323ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-169MS` (url=435ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS` (url=298ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-170MS` (url=262ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-296MS` (url=620ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-320MS` (url=683ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-317MS` (url=622ms, status=HTTP 204)
23. `AKUN-024-WPENG-VLESS-WS-327MS` (url=812ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-338MS` (url=671ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-346MS` (url=749ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
