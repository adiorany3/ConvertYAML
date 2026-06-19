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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=211ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=201ms, nekobox=181ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-123MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-116MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-267MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-250MS`
9. `AKUN-008-MICROSOFT-VLESS-WS-253MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-265MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-301MS` (url=3978ms, nekobox=381ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS`
13. `AKUN-016-UNKNOWN-VLESS-WS-280MS` (url=568ms, status=HTTP 204)
14. `AKUN-017-UNKNOWN-VLESS-WS-377MS` (url=556ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-121MS` (url=202ms, status=HTTP 204)
16. `AKUN-019-UNKNOWN-VLESS-WS-374MS` (url=560ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-394MS` (url=562ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-382MS` (url=565ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-383MS` (url=699ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-96MS` (url=241ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-254MS` (url=535ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
